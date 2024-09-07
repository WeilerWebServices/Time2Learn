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

import java.text.MessageFormat;
import java.util.Random;


public class Game5min extends Activity {

    public TimeObject currentTime;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_game5min);

        refreshScreen();
        Spinner spinner = (Spinner) findViewById(R.id.spinnerQuarters);
        ArrayAdapter<CharSequence> adapter = ArrayAdapter.createFromResource(this,R.array.time_repstring, android.R.layout.simple_spinner_item);
        adapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
        spinner.setAdapter(adapter);

        Spinner spinner1 = (Spinner) findViewById(R.id.spinnerNumbers);
        ArrayAdapter<CharSequence> adapter1 = ArrayAdapter.createFromResource(this,R.array.time_numbers, android.R.layout.simple_spinner_item);
        adapter1.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
        spinner1.setAdapter(adapter1);

        Spinner spinner2 = (Spinner) findViewById(R.id.spinner5min);
        ArrayAdapter<CharSequence> adapter2 = ArrayAdapter.createFromResource(this,R.array.time_5mins, android.R.layout.simple_spinner_item);
        adapter2.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
        spinner2.setAdapter(adapter2);

        Button butCheck = (Button) findViewById(R.id.butCheckAnswer5min);
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
        getMenuInflater().inflate(R.menu.game5min, menu);
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

    public void drawClock(){
        MyAnalogClock clock = (MyAnalogClock) findViewById(R.id.clock5minGame);
        currentTime = randomTime();
        Log.d("GameTAG:", MessageFormat.format("Hours: {0} Minutes: {1} String: {2}", currentTime.hours, currentTime.minutes, currentTime.stringRep));
        clock.setTime(currentTime.hours, currentTime.minutes, 0);
        clock.invalidate();
    }

    public void refreshScreen(){
        TextView txtScore = (TextView) findViewById(R.id.textGottenScore);
        SharedPreferences prefs = getSharedPreferences("time_scores", 0);
        String score = prefs.getString("current_score", "0");
        txtScore.setText(this.getString(R.string.current_score) + " " + score);
        drawClock();
    }

    public TimeObject randomTime(){
        Random random = new Random();
        TimeObject result = new TimeObject(0,0,"");
        result.hours = random.nextInt(12);
        result.minutes = random.nextInt(11) * 5;
        return result;
    }

    public void clickHandler(){
        Spinner spin5mins = (Spinner) findViewById(R.id.spinner5min);
        Spinner spinQuart = (Spinner) findViewById(R.id.spinnerQuarters);
        Spinner spinHours = (Spinner) findViewById(R.id.spinnerNumbers);

        int hours = Integer.parseInt(spinHours.getSelectedItem().toString());
        int minutes = 0;
        String curQuart = spinQuart.getSelectedItem().toString();
        String[] quarts = getResources().getStringArray(R.array.time_repstring);
        if(curQuart.equals(quarts[0]))
            minutes = 0;
        else if(curQuart.equals(quarts[1]))
            minutes = 15;
        else if(curQuart.equals(quarts[2])) {
            minutes = 30;
            hours -= 1;
        } else {
            minutes = 45;
            hours -= 1;
        }

        String cur5min = spin5mins.getSelectedItem().toString();
        String[] mins = getResources().getStringArray(R.array.time_5mins);
        if(cur5min.equals(mins[0]))
            minutes += 5;
        else if(cur5min.equals(mins[1]))
            minutes += 10;
        else if(cur5min.equals(mins[2]))
            minutes -= 10;
        else if(cur5min.equals(mins[3]))
            minutes -= 5;
        else
            minutes = minutes;

        if(minutes == -5) {
            hours -= 1;
            minutes = 55;
        } else if(minutes == -10){
            hours -= 1;
            minutes = 50;
        }
        if(hours == 12)
            hours = 0;

        SharedPreferences prefs = getSharedPreferences("time_scores", 0);
        if(currentTime.hours == hours && currentTime.minutes == minutes){
            Toast.makeText(getApplicationContext(), this.getString(R.string.gratz), Toast.LENGTH_LONG).show();
            int score = Integer.parseInt(prefs.getString("current_score", "0")) + 2;
            prefs.edit().putString("current_score", Integer.toString(score)).apply();
            refreshScreen();
        } else{
            String correctAnswer = "";
            if(currentTime.minutes == 0)
                correctAnswer = mins[4] + " " + quarts[0] + " " + currentTime.hours;
            else if(currentTime.minutes == 5)
                correctAnswer = mins[0] + " " + quarts[0] + " " + currentTime.hours;
            else if(currentTime.minutes == 10)
                correctAnswer = mins[1] + " " + quarts[0] + " " + currentTime.hours;
            else if(currentTime.minutes == 15)
                correctAnswer = mins[4] + " " + quarts[1] + " " + currentTime.hours;
            else if(currentTime.minutes == 20)
                correctAnswer = mins[0] + " " + quarts[1] + " " + currentTime.hours;
            else if(currentTime.minutes == 25)
                correctAnswer = mins[1] + " " + quarts[1] + " " + currentTime.hours;
            else if(currentTime.minutes == 30)
                correctAnswer = mins[4] + " " + quarts[2] + " " + (currentTime.hours + 1);
            else if(currentTime.minutes == 35)
                correctAnswer = mins[0] + " " + quarts[2] + " " + (currentTime.hours + 1);
            else if(currentTime.minutes == 40)
                correctAnswer = mins[1] + " " + quarts[2] + " " + (currentTime.hours + 1);
            else if(currentTime.minutes == 45)
                correctAnswer = mins[4] + " " + quarts[3] + " " + (currentTime.hours + 1);
            else if(currentTime.minutes == 50)
                correctAnswer = mins[0] + " " + quarts[4] + " " + (currentTime.hours + 1);
            else if(currentTime.minutes == 55)
                correctAnswer = mins[1] + " " + quarts[4] + " " + (currentTime.hours + 1);


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
