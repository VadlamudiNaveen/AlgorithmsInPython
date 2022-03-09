import java.util.*;

public class Infix_to_PostFix 
{
	
	 static int Prec(char ch)
	{
	 switch (ch)
	 {
	 case '+':
	 case '-':
	 return 1;
	 
	 case '*':
	 case '/':
	 return 2;
	 
	 case '^':
	 return 3;
	 }
	 return -1;
	}
	 
	 // This Function Will Ensure Whether, the Expression is Correctly formatted or not.
	 public static int checkExpression(String expr, HashMap<String,Integer> map, Set<Integer> set) 
	 {
		 
 	 // O(N) To build the Hash Map 
 	 for (int i = 0; i< expr.length(); i++) 
 	 {
 		char chr = expr.charAt(i);
 		if ( chr == '(' || chr == ')') 
 		{	 
 			 if (map.containsKey(Character.toString(chr))) 
 			 {
 				 		map.put(Character.toString(chr), map.get(Character.toString(chr)) + 1);
 			 }
 			 else 
 			 {
 				 map.put(Character.toString(chr),1);
 			 } 
 		} 			 
 	 }
// This will ensure if the given expression, is correct or not.
 	 for (Map.Entry<String, Integer> e : map.entrySet()) 
 	 {
 		 	 			set.add(e.getValue());
 	 }
		 map.clear();
 	 return set.size();
	 }
	 public static String evaluatePostFix(String expr, HashMap<String,Integer> map) 
	 { 
		/**
		 map.put("^", 3);
		 map.put("*", 2);
		 map.put("/", 2);
		 map.put("+", 1);
		 map.put("-", 1);
		 map.put("(", -1);
		 map.put(")", -1);
		 **/
		 //System.out.println(map.toString());
		 Deque<String> stack = new ArrayDeque<String>();
		 String res = "";
		 for (int i = 0; i< expr.length(); i++) 
		 { 
			 char chr = expr.charAt(i);
			 System.out.println(res.toString());
			 	 if ((int) chr >= 48 && (int) chr <= 57)
			 	 {
			 		 	res += chr; 
			 	 } 
			 	 else
			 	 {	
			 		
			 		/**
			 		if (chr == '(')
			 		{  
			 			System.out.println(chr);
			 				stack.push(Character.toString(chr));
			 		}
			 		**/
			 		/**
			 		if (chr == ')') 
			 		{
			 				while (true) 
			 				{		
			 					if (stack.peek() == "(") 
			 					{
			 						 stack.pop();
			 						 break;
			 					}
			 				 res += stack.pop();	
			 				}
			 		}
			 		**/
			 		 /**
			 		else 
			 		{	
			 		 **/ 	
			 			if (stack.isEmpty()) 
			 			{
			 				stack.push(Character.toString(chr));
				 			System.out.println(stack.toString());
			 			}
			 			else 
			 			{
			 			
			 				//System.out.println((int) stack.peek().charAt(0)+ "" + stack.peek()+ " " + chr+"" + (int) chr);
			 				//System.out.println((int) stack.peek().charAt(0)+ " " + stack.peek() + " "+chr+ "" + (int) chr );
					 		if (( map.get(Character.toString(stack.peek().charAt(0)))> map.get(Character.toString(chr)) ) 
					 		  || ( map.get(Character.toString(stack.peek().charAt(0)))== map.get(Character.toString(chr)) ) 
					 		  )
					 		{  
					 			System.out.println(stack.peek()+chr);
					 					res += stack.pop();
					 					stack.push(Character.toString(chr));
					 		}
					 		
					 				
					 		 
					 		/**
					 		if (map.get(stack.peek()) < map.get(Character.toString(chr))) 
					 		{
					 			 
					 		}	  stack.push(Character.toString(chr));
			 			**/
			 			}
			 			
	
			 		}
			 		
			 		/**
			 		if (stack.peek().equals("("))
			 		{
			 		}
			 		**/
			 		 
			 	 }
		 
		 return res; 
	 }
public static void main(String args[]) 
{
Scanner sc = new Scanner(System.in);
System.out.println("\n");
			 System.out.println("Enter the Mathematical Expression:");
HashMap<String, Integer> map = new HashMap<>();
	 Set<Integer> set = new HashSet<Integer> (); 


			 if (sc.hasNext())
{
 	 String expr = sc.next();
 	 if (checkExpression(expr, map, set) == 1) 
 	 {
 		 System.out.println(evaluatePostFix(expr,map));
 	 }
 	 else 
 	 {
 		 System.out.println("The Expression is invalid \n");
 	 } 	 
 	 
}
else 
{
 System.out.println("Hey try to enter the Mathematical Expression as String\n");	 
}
}
}