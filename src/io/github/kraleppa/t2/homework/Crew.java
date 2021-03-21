package io.github.kraleppa.t2.homework;

import com.rabbitmq.client.*;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.charset.StandardCharsets;

public class Crew {
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private final static String productExchange = "products";
    private final static String messageExchange = "messages";
    private static String name = "";

    public static void main(String[] argv) throws Exception {
        System.out.println("Podaj nazwe ekipy: ");
        String name = br.readLine();

        ConnectionFactory factory = new ConnectionFactory();
        factory.setHost("localhost");
        Connection connection = factory.newConnection();
        Channel channel = connection.createChannel();

        channel.exchangeDeclare(messageExchange, BuiltinExchangeType.DIRECT);

        channel.queueDeclare(name + "_queue", false, false, false, null);
        channel.queueBind(name + "_queue", messageExchange, name);
        channel.queueBind(name + "_queue", messageExchange, "crews");
        channel.queueBind(name + "_queue", messageExchange, "all");

        Consumer consumer = new DefaultConsumer(channel) {
            @Override
            public void handleDelivery(String consumerTag, Envelope envelope, AMQP.BasicProperties properties, byte[] body) throws IOException {
                String message = new String(body, StandardCharsets.UTF_8);
                System.out.println("Received: " + message);
                channel.basicAck(envelope.getDeliveryTag(), false);
            }
        };


        channel.basicConsume(name + "_queue", false, consumer);

        while (true) {

            // read msg
            System.out.println("Enter key: ");
            String key = br.readLine();
            if (key.equals("exit")) {
                break;
            }
            // publish
            channel.basicPublish(productExchange, key, null, name.getBytes(StandardCharsets.UTF_8));
        }
    }
}
