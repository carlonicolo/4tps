package primaLezione;

public class Animale {
    private String nome;
    private int eta;
    private float peso;
    private int num_zampe;

    public Animale(String nome, int eta, int peso, int num_zampe) {
        this.eta = eta;
        this.peso = peso;
        this.num_zampe = num_zampe;
    }

    public Animale(int eta, int peso, int num_zampe) {
        this.eta = eta;
        this.peso = peso;
        this.num_zampe = num_zampe;
    }

    public void abbaia(){
        System.out.println("Bau Bau");
    }

    public String salutaNome(String nome){
        String saluto = "Ciao " + nome ;
        return saluto;
    }


}
