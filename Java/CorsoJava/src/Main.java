import primaLezione.*;

public class Main {
    public static void main(String[] args) {
        //System.out.println("Hello world!");
        Animale pluto = new Animale(5,80,4);
        pluto.abbaia();
        String s = pluto.salutaNome("4INF");
        System.out.println(s);

        System.out.println("###############");

        Animale zig = new Animale("Zig",5,80,4);
        zig.abbaia();
        String sal = zig.salutaNome("Kevin");
        System.out.println(sal);
    }
}