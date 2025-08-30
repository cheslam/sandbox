# Export Chat Snippet (for browser console)

Use this in ChatGPT’s Console (F12) after scrolling to the top of the chat.  
It will download the conversation as a Markdown file.
**make sure to change** `const filename = "week_XX_log.md` **to current week in the console**

```js
(async () => {
  const sleep = ms => new Promise(r => setTimeout(r, ms));
  for (let i = 0; i < 20; i++) {
    window.scrollTo(0, 0);
    await sleep(300);
    if (window.scrollY === 0) break;
  }

  // Custom filename: week_XX_log.md
  const date = new Date().toISOString().slice(0,10);
  const filename = "week_XX_log.md";

  const nodes = Array.from(document.querySelectorAll('[data-message-author-role]'));
  const parts = nodes.map(n => {
    const role = n.getAttribute('data-message-author-role');
    const speaker = role === 'user' ? 'User' : 'Assistant';
    const text = n.innerText.trim();
    return `**${speaker}:**\n\n${text}`;
  });

  const md = `# Chat Log\n**Date:** ${date}\n\n---\n${parts.join('\n\n---\n\n')}\n`;

  const blob = new Blob([md], { type: "text/markdown" });
  const url = URL.createObjectURL(blob);
  const a = document.createElement("a");
  a.href = url;
  a.download = filename;
  document.body.appendChild(a);
  a.click();
  a.remove();
  URL.revokeObjectURL(url);
  console.log("Downloaded", filename);
})();
```
