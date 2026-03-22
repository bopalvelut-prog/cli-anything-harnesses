import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def run(): subprocess.run(['v2ray', 'run', '-c', 'config.json'])
@cli.command()
def test(): subprocess.run(['v2ray', 'test', '-c', 'config.json'])
@cli.command()
def version(): subprocess.run(['v2ray', 'version'])
if __name__ == '__main__': cli()
