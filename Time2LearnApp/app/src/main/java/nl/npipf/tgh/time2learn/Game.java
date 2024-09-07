package nl.npipf.tgh.time2learn;

import android.app.Activity;
import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.util.Log;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.Spinner;
import android.widget.TextView;
import android.widget.Toast;

import org.w3c.dom.Text;

import java.text.MessageFormat;
import java.util.Random;


public class Game extends Activity {

    TimeObject currentTime;
    Random random = new Random();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_game);

        refreshScreen();
        Spinner spinner = (Spinner) findViewById(R.id.spinnerRepString);
        ArrayAdapter<CharSequence> adapter = ArrayAdapter.createFromResource(this,R.array.time_repstring, android.R.layout.simple_spinner_item);
        adapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
        spinner.setAdapter(adapter);

        Spinner spinner1 = (Spinner) findViewById(R.id.spinnerNumber);
        ArrayAdapter<CharSequence> adapter1 = ArrayAdapter.createFromResource(this,R.array.time_numbers, android.R.layout.simple_spinner_item);
        adapter1.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
        spinner1.setAdapter(adapter1);

        Button butCheck = (Button) findViewById(R.id.butCheckAnswer);
        butCheck.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                clickHandler();
            }
        });
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.game, menu);
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

    public TimeObject randomTime(){
        TimeObject result = new TimeObject(0, 0, "");
        result.hours = random.nextInt(12);
        result.minutes = (random.nextInt(3) * 15);
        return result;
    }

    public void drawClock(){
        MyAnalogClock clock = (MyAnalogClock) findViewById(R.id.clockGame);
        currentTime = randomTime();
        Log.d("GameTAG:", MessageFormat.format("Hours: {0} Minutes: {1} String: {2}", currentTime.hours, currentTime.minutes, currentTime.stringRep));
        clock.setTime(currentTime.hours, currentTime.minutes, 0);
        clock.invalidate();
    }

    public void refreshScreen(){
        TextView txtScore = (TextView) findViewById(R.id.textCurScore);
        SharedPreferences prefs = getSharedPreferences("time_scores", 0);
        String score = prefs.getString("current_score", "0");
        txtScore.setText(this.getString(R.string.current_score) + " " + score);
        drawClock();
    }

    public void clickHandler(){
        Spinner spinNumber = (Spinner) findViewById(R.id.spinnerNumber);
        Spinner spinRep = (Spinner) findViewById(R.id.spinnerRepString);

        int hours = Integer.parseInt(spinNumber.getSelectedItem().toString());
        String rep = spinRep.getSelectedItem().toString();
        String[] reps = getResources().getStringArray(R.array.time_repstring);
        int mins = 0;
        String correctAnswer;
        if(rep.equals(reps[0]))
            mins = 0;
        else if(rep.equals(reps[1]))
            mins = 15;
        else if (rep.equals(reps[2])) {
            mins = 30;
            hours -= 1;
        } else {
            mins = 30;
            hours -= 1;
        }
        if (hours == 0)
            hours = 12;
        SharedPreferences prefs = getSharedPreferences("time_scores", 0);
        if (currentTime.hours == hours && currentTime.minutes == mins) {
            Toast.makeText(getApplicationContext(), this.getString(R.string.gratz) , Toast.LENGTH_LONG).show();
            int score = Integer.parseInt(prefs.getString("current_score", "0")) + 1;
            prefs.edit().putString("current_score", Integer.toString(score)).apply();
            refreshScreen();
        } else{
            if (currentTime.minutes == 0)
                correctAnswer = reps[0] + " " + currentTime.hours;
            else if (currentTime.minutes == 15)
                correctAnswer = reps[1] + " " + currentTime.hours;
            else if (currentTime.minutes == 30)
                correctAnswer = reps[2] + " " + (currentTime.hours + 1);
            else
                correctAnswer = reps[3] + " " + (currentTime.hours + 1);


            Toast.makeText(getApplicationContext(), this.getString(R.string.lost) , Toast.LENGTH_LONG).show();
            int score = Integer.parseInt(prefs.getString("current_score", "0"));
            int highscore = Integer.parseInt(prefs.getString("highscore", "0"));
            prefs.edit().putString("current_score", "0").apply();
            if(score > highscore)
                prefs.edit().putString("highscore", Integer.toString(score)).apply();
            Intent intent = new Intent(getApplicationContext(), EndScreen.class);
            intent.putExtra("correct_answer", correctAnswer);
            intent.putExtra("current_score", score);
            refreshScreen();
            startActivity(intent);
        }
    }
}
