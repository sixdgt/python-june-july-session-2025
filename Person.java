class Person(){
    // private attributes
    private String name;
    private int age;
    // protected attributes
    protected String address;
    protected String phoneNumber;

    public String email;

    public void setName(String name){
        this.name = name;
    }

    public String getName(){
        return this.name;
    }

    public static void main(String args[]){

        Person p = new Person();
        p.setName("John Doe");
        System.out.println("Name: " + p.getName());
    }
}