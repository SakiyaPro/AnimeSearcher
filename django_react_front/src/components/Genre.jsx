import React from "react";
import moving from "../static/img/ジャンル(感動).jpg";
import comedy from "../static/img/ジャンル(ギャグ・日常).jpg";
import sf from "../static/img/ジャンル(SF).png";
import battle from "../static/img/ジャンル(バトル).jpg";


export const Genre = () => {
    return (
        <section id="genre-content">
            <p>ジャンルで絞る</p>
            <ul>
                <li>
                    <a href="/">
                        <img src={moving} alt="感動" />
                        <h3>感動</h3>
                    </a>
                </li>
                <li>
                    <a href="/">
                        <img src={comedy} alt="ギャグ・日常" />
                        <h3>日常</h3>
                    </a>
                </li>
                <li>
                    <a href="/">
                        <img src={sf} alt="SF" />
                        <h3>SF</h3>
                    </a>
                </li>
                <li>
                    <a href="/">
                        <img src={battle} alt="バトル" />
                        <h3>バトル</h3>
                    </a>
                </li>
            </ul>
        </section>
    );
};