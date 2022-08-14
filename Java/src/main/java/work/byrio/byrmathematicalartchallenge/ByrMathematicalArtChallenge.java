package work.byrio.byrmathematicalartchallenge;

public class ByrMathematicalArtChallenge {
    public static void main(String[] args) {
        Render render = new Render();
        String output_path = "output.gif";
        if (args.length > 0) {
            output_path = args[0];
        }
        render.render(output_path);
    }
}
