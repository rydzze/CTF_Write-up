# [Rev] Intro to Unity

## 📚 Overview

> *"( right mouse to play player 1 and spacebar to play player 2 ) please make an internal cheats that get 100 score and maphack, im very tired getting lose and lose again"*

## ✨ Walkthrough

Given a .ZIP file, which turned out to be a folder containing Unity game with assets, the *Flappy Bird*. We need the score of 100 to win and get the flag but *doing it manually would take some time*. That said, let's do some mods on the `Assembly-CSharp.dll`, which "*is a predefined assembly that compiles most game scripts by default*". The file can be found inside `Windows-Releae\FlappySec_Data\Managed` directory.

In this case, let's use [dnSpy](https://github.com/dnSpy/dnSpy) to modify the file. Most of the game scripts can be found inside `Assembly-CSharp (0.0.0.0) > Assembly-CSharp.dll > -`

### 1. Modify the `ScoringSystem` class.

Increase the stepsize from 1 to 100.

```csharp
public void UpdateScore()
{
	this.score += 100;
	this.currScoreText.text = this.score.ToString();
	this.UpdateTopScore();
}
```

### 2. Modify the `GameManager` class.

Change the height and width of the window.

```csharp
public void Start()
{
	Screen.SetResolution((int)((float)Screen.height * 1f), Screen.height, false);
	Screen.SetResolution((int)((float)Screen.width * 2f), Screen.width, false);
}
```

### 3. Modify the `FlyBehaviour` class.

*Immortality*, remove/comment the `GameManager.Instance.GameOver()` to avoid game over.

```csharp
private void OnCollisionEnter2D(Collision2D collision)
{
	// GameManager.Instance.GameOver();
}
```

## 🏳️ Flag

`TCP1P{sc0r3_1s_d4ng3r0us_w1th_pr3fs}`