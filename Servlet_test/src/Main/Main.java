package Main;

import java.awt.Desktop;
import java.io.File;


public class Main{
   
   //Java Program to Open the given URL in System Default Browser in Windows
   public static void main(String[] args) {
//	   Path "C:\\Users\\gnom5\\OneDrive\\Desktop\\Hello World.html"
	   
	
	   try  
	   {  
	   //constructor of file class having file as argument  
	   File file = new File("C:\\Users\\gnom5\\OneDrive\\Desktop\\Hello World.html");   
	   if(!Desktop.isDesktopSupported())//check if Desktop is supported by Platform or not  
	   {  
	   System.out.println("not supported");  
	   return;  
	   }  
	   Desktop desktop = Desktop.getDesktop();  
	   if(file.exists())         //checks file exists or not  
	   desktop.open(file);              //opens the specified file  
	   }  
	   catch(Exception e)  
	   {  
	   e.printStackTrace();  
	   }  
	   }
   }
