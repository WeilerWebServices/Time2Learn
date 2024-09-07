package nl.npipf.tgh.time2learn;

import android.app.Activity;
import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import org.w3c.dom.Text;


public class MainMenu extends Activity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main_menu);

        refreshHighscore();

        Button butStartGame = (Button) findViewById(R.id.butStartGame);
        butStartGame.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(getApplicationContext(), Game.class);
                startActivity(intent);
            }
        });

        Button butStart5minGame = (Button) findViewById(R.id.butStart5Min);
        butStart5minGame.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(getApplicationContext(), Game5min.class);
                startActivity(intent);
            }
        });
    }

    public void refreshHighscore() {
        SharedPreferences prefs = getSharedPreferences("time_scores", 0);
        String Highscore = prefs.getString("highscore", this.getString(R.string.highscore_default));
        TextView txtHighscore = (TextView) findViewById(R.id.textHighscore);
        txtHighscore.setText("Highscore: " + Highscore);
    }


    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.main_menu, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();
        if (id == R.id.menuCredits) {
            Intent intent = new Intent(getApplicationContext(), Credits.class);
            startActivity(intent);
            return true;
        }
        return super.onOptionsItemSelected(item);
    }

    @Override
    public void onResume() {
        super.onResume();
        refreshHighscore();
    }
}
