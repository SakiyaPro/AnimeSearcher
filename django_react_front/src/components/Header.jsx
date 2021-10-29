import React from "react";

export const Header = (props) => {
    const { headertext } = props;
    return (
        <header>
            <h1><a href="/">{headertext}</a></h1>
            <nav className="app-nav">
                <ul>
                    <li><a href="/">2021秋アニメ</a></li>
                    <li><a href="/">2021夏アニメ</a></li>
                    <li><a href="/">人気アニメ</a></li>
                </ul>
            </nav>
        </header>
    );
}