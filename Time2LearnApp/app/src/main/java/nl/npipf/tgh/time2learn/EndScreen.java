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


public class EndScreen extends Activity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_end_screen);

        SharedPreferences prefs = getSharedPreferences("time_scores", 0);
        String highscore = prefs.getString("highscore", "0");
        TextView txtHighscore = (TextView) findViewById(R.id.textHighscoreEnd);
        txtHighscore.setText("Highscore: " + highscore);

        Intent intent = getIntent();

        String correctAnswer = intent.getStringExtra("correct_answer");
        TextView txtCorrectAnswer = (TextView) findViewById(R.id.textCorrectAnswer);
        txtCorrectAnswer.setText(correctAnswer);

        int currentScore = intent.getIntExtra("current_score", 0);
        TextView txtCurrentScore = (TextView) findViewById(R.id.textGottenScore);
        txtCurrentScore.setText(this.getString(R.string.current_score) + " " + currentScore);

        Button butTryAgain = (Button) findViewById(R.id.butTryAgain);
        butTryAgain.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                finish();
            }
        });
    }


    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.end_screen, menu);
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
}
