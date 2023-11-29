package primaLezione;

public class Animale {
    private int eta;
    private float peso;
    private int num_zampe;

    public Animale(int eta, int peso, int num_zampe) {
        this.eta = eta;
        this.peso = peso;
        this.num_zampe = num_zampe;
    }

    public void abbaia(){
        System.out.println("Bau Bau");
    }

    public String greeting(String nome){
        String saluto = "Ciao " + nome ;
        return saluto;
    }


}
