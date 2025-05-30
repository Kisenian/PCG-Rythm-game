using System.Collections.Generic;
using UnityEngine;
using System.IO;

[System.Serializable]
public class RhythmData {
    public List<float> bass;
    public List<float> snare;
}

public class LevelGenerator : MonoBehaviour {
    public TextAsset rhythmJson;
    public GameObject bassPlatformPrefab;
    public GameObject snareEnemyPrefab;

    public float unitsPerSecond = 2f;

    void Start() {
        RhythmData data = JsonUtility.FromJson<RhythmData>(rhythmJson.text);

        foreach (float bassTime in data.bass) {
            Vector3 position = new Vector3(bassTime * unitsPerSecond, 0, 0);
            Instantiate(bassPlatformPrefab, position, Quaternion.identity);
        }

        foreach (float snareTime in data.snare) {
            Vector3 position = new Vector3(snareTime * unitsPerSecond, 1, 0);
            Instantiate(snareEnemyPrefab, position, Quaternion.identity);
        }
    }
}
