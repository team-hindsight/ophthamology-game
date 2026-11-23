# EyeCanDo

EyeCanDo is a 3D game for iOS and Android mobile devices that helps children
prepare for an eye clinic visit. Through guided activities, children learn what
to expect during an eye exam and practise taking part at their own pace.

## Setup and run

You’ll need Git, Unity Hub, and Unity **6000.6.2f1**.

```sh
git clone https://github.com/team-hindsight/ophthamology-game.git
cd ophthamology-game
```

1. In Unity Hub, choose **Add → Add project from disk** and select `src/EyeCanDo`.
2. Open the project and wait for Unity to finish importing it.
3. Open `Assets/_Project/Scenes/Menu.unity` in the Unity editor and select **Play**.

## Build for a device

- **Android** — Install Android Build Support with the SDK, NDK, and OpenJDK
  modules in Unity Hub. In the editor, choose **POC → Build Android APK**. The
  APK appears at `Builds/Android/EyeCanDo.apk` inside the Unity project.
- **iOS** — Install iOS Build Support. In **File → Build Profiles**, add and
  switch to an iOS profile, then select **Build** to export an Xcode project.
  Build and sign the project in Xcode on macOS to install it on an iPhone or iPad.
  [Unity iOS build guide](https://docs.unity.com/en-us/engine/6000.6/manual/platform-specific/iphone/ios-building-and-delivering/build-process)

## Run the tests

In Unity, open **Window → General → Test Runner**, select **EditMode**, and click
**Run All**.

## Project documentation

[View the project documentation on GitHub Pages](https://team-hindsight.github.io/ophthamology-game/).

## Repository structure

| Path | Contents |
| --- | --- |
| [`src/EyeCanDo/`](src/EyeCanDo) | Unity project, including game code, scenes, and assets |
| [`src/EyeCanDo/Assets/_Project/Tests/EditMode/`](src/EyeCanDo/Assets/_Project/Tests/EditMode) | Unity Edit Mode tests |
| [`docs/`](docs) | LaTeX sources for the project documentation |
| [`pdfs/`](pdfs) | Generated project documentation |
| [`refs/`](refs) | Project references and bibliography |
| [`site/`](site) | GitHub Pages template and stylesheet |
| [`.github/`](.github) | Documentation workflow and repository templates |

## Team and license

Team Hindsight is Ahsan Muzammil, Mohammad Bilal, Jackson Beach, Ethan McMehen,
and Jake Finlay.

The project code is available under the [MIT License](LICENSE). See the
[third-party asset credits](src/EyeCanDo/THIRD_PARTY_ASSETS.md) for asset-specific terms.
