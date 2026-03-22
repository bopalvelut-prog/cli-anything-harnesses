import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def run(): subprocess.run(['sing-box', 'run', '-c', 'config.json'])
@cli.command()
def check(): subprocess.run(['sing-box', 'check', '-c', 'config.json'])
@cli.command()
def version(): subprocess.run(['sing-box', 'version'])
if __name__ == '__main__': cli()
