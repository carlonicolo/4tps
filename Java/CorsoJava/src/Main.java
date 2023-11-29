import primaLezione.*;

public class Main {
    public static void main(String[] args) {
        //System.out.println("Hello world!");
        Animale pluto = new Animale(5,80,4);
        pluto.abbaia();
        String s = pluto.greeting("4INF");
        System.out.println(s);
    }
}