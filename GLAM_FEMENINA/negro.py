import java.util.ArrayList;
import java.util.Scanner;

class Usuario {
    private String usuario;
    private String nombre;
    private String contrasena;

    public Usuario(String usuario, String nombre, String contrasena) {
        this.usuario = usuario;
        this.nombre = nombre;
        this.contrasena = contrasena;
    }

    public String getUsuario() {
        return usuario;
    }

    public String getNombre() {
        return nombre;
    }

    @Override
    public String toString() {
        return "Usuario{" +
                "usuario='" + usuario + '\'' +
                ", nombre='" + nombre + '\'' +
                '}';
    }
}

public class RegistroUsuarios {
    private static ArrayList<Usuario> usuarios = new ArrayList<>();

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        boolean continuar = true;

        while (continuar) {
            System.out.println("=== Registro de Usuarios ===");
            System.out.print("Ingrese su nombre de usuario: ");
            String usuario = scanner.nextLine();

            System.out.print("Ingrese su nombre completo: ");
            String nombre = scanner.nextLine();

            System.out.print("Ingrese su contraseña: ");
            String contrasena = scanner.nextLine();

            // Crear un nuevo usuario
            Usuario nuevoUsuario = new Usuario(usuario, nombre, contrasena);
            usuarios.add(nuevoUsuario);

            System.out.println("Usuario registrado exitosamente.");

            System.out.print("¿Desea registrar otro usuario? (s/n): ");
            String respuesta = scanner.nextLine();
            if (!respuesta.equalsIgnoreCase("s")) {
                continuar = false;
            }
        }

        System.out.println("\nUsuarios registrados:");
        for (Usuario user : usuarios) {
            System.out.println(user);
        }

        scanner.close();
    }
