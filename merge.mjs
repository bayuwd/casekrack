import fs from 'fs';

const c1 = JSON.parse(fs.readFileSync('chunk_1.json', 'utf8'));
const c2 = JSON.parse(fs.readFileSync('chunk_2.json', 'utf8'));
const c3 = JSON.parse(fs.readFileSync('chunk_3.json', 'utf8'));
const c4 = JSON.parse(fs.readFileSync('chunk_4.json', 'utf8'));
const c5 = JSON.parse(fs.readFileSync('chunk_5.json', 'utf8'));
const c6 = JSON.parse(fs.readFileSync('chunk_6.json', 'utf8'));

const allBriefs = [...c1, ...c2, ...c3, ...c4, ...c5, ...c6];

fs.writeFileSync('src/data/briefs.js', 'export const briefs = ' + JSON.stringify(allBriefs, null, 2) + ';\n');

try { fs.unlinkSync('chunk_1.json'); } catch(e){}
try { fs.unlinkSync('chunk_2.json'); } catch(e){}
try { fs.unlinkSync('chunk_3.json'); } catch(e){}
try { fs.unlinkSync('chunk_4.json'); } catch(e){}
try { fs.unlinkSync('chunk_5.json'); } catch(e){}
try { fs.unlinkSync('chunk_6.json'); } catch(e){}
try { fs.unlinkSync('shard.mjs'); } catch(e){}
console.log('Successfully merged all chunks back into briefs.js and cleaned up.');
