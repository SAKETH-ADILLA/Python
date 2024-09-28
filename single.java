class A{
    void display(){
        System.out.println("Class A");
    }
}
class B extends A{
    void display1(){
        System.out.println("Class B");
    }
}
class single{
    public static void main(String args[]){
        B a= new B();
        a.display();
        a.display1();

    }
}