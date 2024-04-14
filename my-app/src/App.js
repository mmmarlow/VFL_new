import "./App.css";
import logo from './logo.png';

function App() {

  return (

    <div>
      <header className="header">
        <nav className="inner-header">
          <img src={logo} alt="Logo" className="main-page-header-logo"></img>
          <ul className="nav-list">
            <li id="create-team-nav-button">
              <a href="#" onclick="createTeam(); return false;">Create Team</a>
            </li>
            <li id="view-team-nav-button">
              <a href="#" onclick="viewTeam(); return false;">View Team</a>
            </li>
            <li id="stats-nav-button">
              <a href="#" onclick="stats(); return false;">Stats</a>
            </li>
            <li id="leaderboard-nav-button">
              <a href="#" onclick="leaderboard(); return false;">Global Leaderboard</a>
            </li>
            <li id="forums-nav-button">
              <a href="#" onclick="forums(); return false;">Forums</a>
            </li>
          </ul>
        </nav>
      </header>
      <div id="wrapper">
        <div id="main-page-text">
          <h1 id="main-page-title">A New Premier Valorant Fantasy League</h1>
          <p id="main-page-para">Create Team! Compete! Score!</p>
        </div>
      </div>
      <div className="footer">

      </div>
    </div>

  );

}

function createTeam() {

  return (

    null

  );

}

function viewTeam() {

  return (

    null

  );

}

function stats() {

  return (

    null

  );

}

function leaderboard() {

  return (

    null

  );

}

function forums() {

  return (

    null

  );

}

export default App;