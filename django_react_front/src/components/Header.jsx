import React from "react";

export const Header = (props) => {
    const { headertext } = props;
    console.log(props);
    return (
        <nav className="App-Header">
            <a href="/">{headertext}</a>
            <ul style={{ display: 'flex', listStyle: 'none' }}>
                <li><a href="https://www.google.com/">2021秋アニメ</a></li>
                <li><a href="https://www.google.com/">2021夏アニメ</a></li>
                <li><a href="https://www.google.com/">人気アニメ</a></li>
            </ul>
        </nav>
    );
}