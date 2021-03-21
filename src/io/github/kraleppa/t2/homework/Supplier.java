package io.github.kraleppa.t2.homework;

import com.rabbitmq.client.*;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.List;
import java.util.UUID;

public class Supplier {

    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private final static String productExchange = "products";
    private final static String messageExchange = "messages";
    private final static List<String> products = new ArrayList<>();

    public static void main(String[] args) throws Exception {
        System.out.println("Podaj nazwe dostawcy: ");
        String name = br.readLine();

        ConnectionFactory factory = new ConnectionFactory();
        factory.setHost("localhost");
        Connection connection = factory.newConnection();
        Channel channel = connection.createChannel();

        channel.exchangeDeclare(productExchange, BuiltinExchangeType.DIRECT);
        channel.basicQos(1);


        while (true) {
            System.out.println("Item name: ");
            String product = br.readLine();
            if (product.equals("con")) {
                break;
            }
            products.add(product);
        }


        for (String product : products){
            channel.queueDeclare(product + "_queue", false, false, false, null);
            channel.queueBind(product + "_queue", productExchange, product);
        }

        channel.exchangeDeclare(messageExchange, BuiltinExchangeType.DIRECT);
        channel.queueDeclare(name + "_queue", false, false, false, null);
        channel.queueBind(name + "_queue", messageExchange, name);
        channel.queueBind(name + "_queue", messageExchange, "suppliers");
        channel.queueBind(name + "_queue", messageExchange, "all");


        Consumer consumer = new DefaultConsumer(channel) {
            @Override
            public void handleDelivery(String consumerTag, Envelope envelope, AMQP.BasicProperties properties, byte[] body) throws IOException {
                String message = new String(body, StandardCharsets.UTF_8);
                UUID uuid = UUID.randomUUID();
                System.out.println("Received new order: " + message);
                String responseMessage = "Order for " + message + " " + uuid.toString() + " completed";
                channel.basicPublish(messageExchange, message, null, responseMessage.getBytes());
                channel.basicAck(envelope.getDeliveryTag(), false);
            }
        };

        for (String product : products){
            channel.basicConsume(product + "_queue", false, consumer);
        }
        channel.basicConsume(name + "_queue", false, consumer);
        System.out.println("Waiting for messages...");
    }

}
