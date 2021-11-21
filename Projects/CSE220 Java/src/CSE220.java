
public class CSE220 {

    /**
     * @param args the command line arguments
     */
//    public static int[] reverse(int[] arr){
//        int[] newArr = new int [arr.length];
//        int ind = arr.length-1;
//        for(int item:arr){
//            newArr[ind] = item;
//            ind--;
//        }
//        return newArr;
//    }
     public static void reverse(int[] arr){
         int temp;
        for(int i=0,j=arr.length-1;i<j;i++,j--){
            temp = arr[i];
            arr[i]=arr[j];
            arr[j]=temp;
//            print(arr);
        }
    }
     public static void rShift(int[] arr, int key){
         
         for(int i=arr.length-1;i>=key;i--){
             arr[i] = arr[i-key];
         }
         int i = 0;
         while(i<key){
             arr[i] = 0;
             i++;
         }
         
     }
     public static void rRotate(int[] arr,int key){
         int [] temp = new int[key];
         for(int i=arr.length-1,j=0; i>=key; i--,j++){
             if(j<key){
                temp[j] = arr[i];
             }
             arr[i] = arr[i-key];
         }
         for(int i=0,j=key-1;i<key;i++,j--){
             arr[i] = temp[j];
         }
         
     }
     public static void main(String[] args) {
        int [] source = {10,20,30,40,50,60,70};
        
        print(source);
        System.out.println("------");
//        source = reverse(source);
//        reverse(source);
//        rShift(source,4);
        rRotate(source,1);
        
        print(source);


        
        
            
        
        
    }
public static void print(int a []){
//    for(int i =0;i<a.length;i++){
//            System.out.print(a[i]);
//        }
    for (int x:a){
            System.out.print(x);
            System.out.print(" ");
        }
    System.out.println("");
}
}
