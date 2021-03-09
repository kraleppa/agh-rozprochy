package io.github.kraleppa.t1.lab.zad3;

import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.nio.ByteBuffer;
import java.util.Arrays;

public class JavaUdpServer {

    public static void main(String args[])
    {
        System.out.println("JAVA UDP SERVER");
        DatagramSocket socket = null;
        int portNumber = 9008;

        try{
            socket = new DatagramSocket(portNumber);
            byte[] receiveBuffer = new byte[1024];

            while(true) {
                Arrays.fill(receiveBuffer, (byte)0);
                DatagramPacket receivePacket = new DatagramPacket(receiveBuffer, receiveBuffer.length);
                socket.receive(receivePacket);
                int nb = ByteBuffer.wrap(receiveBuffer).getInt();
                System.out.println("received msg: " + nb);
                nb++;

                byte[] responseBuffer = new byte[1024];
                Arrays.fill(responseBuffer, (byte)0);

                responseBuffer = ByteBuffer.allocate(4).putInt(nb).array();

                DatagramPacket response = new DatagramPacket(responseBuffer,
                        responseBuffer.length,
                        receivePacket.getAddress(),
                        receivePacket.getPort());

                socket.send(response);
            }
        }
        catch(Exception e){
            e.printStackTrace();
        }
        finally {
            if (socket != null) {
                socket.close();
            }
        }
    }
}
