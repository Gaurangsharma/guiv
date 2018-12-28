<%@ page import="java.util.*"%>
<%@ page import="java.sql.*"%>
<%@ page import="java.util.io.*"%>
<%
try{
    String name=Request.getParemeter("name");
    String email=Request.getParemeter("email");
    String phone=Request.getParemeter("phone");
    String password=Request.getParemeter("password");

    Class.forName("com.mysql.jdbc.Driver");
    Connection con=DriverManager.getConnection("jdbc:mysql://localhost:3306/mydata","root","root");
    Statement st=con.createConnection();
    ResultSet rs=st.executeQuery("insert into user (name,email,phone,password) values('"+name+"','"+email+"' '"+phone+"' '"+password+"')");
    if (rs!=null){
        out.println("done");
    }
    else{
        out.println("not done");
    }
}
%>