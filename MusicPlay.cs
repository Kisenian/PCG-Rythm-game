using UnityEngine;

public class MusicPlayer : MonoBehaviour {
    public AudioSource music;

    void Start() {
        music.Play();
    }
}
