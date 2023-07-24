import java.util.Scanner;

public class find_if{
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        System.out.print("string->");
        String s = input.next();
        System.out.print("num->");
        int num=input.nextInt();
        input.close();
        if (num==1) {
            System.out.println("num=1 is running");
        }
        else {
            System.out.println("num=1 is not running"); 
        }

        if (s.equals("we")) {
            System.out.println("s=we is running");
        } else {
            System.out.println("s=we is not running");
        }
    }
}