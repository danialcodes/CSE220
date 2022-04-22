/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Other/File.java to edit this template
 */

/**
 *
 * @author Danial Codes
 */
public class insertion {

    /**
     * @param args the command line arguments
     */
    public static void insert(int [] arr,int size,int index, int value){
        if(arr.length != size){
            for (int i = size; i > index; i--) {
            arr[i]=arr[i-1];
            }
            arr[index] = value;
        }
        
    }
    public static void remove(int [] arr,int size,int index){
        if(arr.length != size){
            for (int i = index; i < size; i++) {
            arr[i]=arr[i+1];
            }
            arr[size] = 0;
        }
        
    }
    public static void print(int [] arr){
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i]);
            System.out.print(" ");
        }
        System.out.println("");
    }
    public static void main(String args[]) {
        // TODO code application logic here
        int [] myArr = {10,20,30,40,50,0,0,0};
        print(myArr);
        System.out.println("-----------------");
        insert(myArr,5,2,100);
        print(myArr);
        System.out.println("-----------------");
        remove(myArr,5,5);
        print(myArr);
         
        
    }
}
