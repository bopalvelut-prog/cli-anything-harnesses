import click, subprocess
@click.group()
def cli(): pass
@cli.command()
@click.argument('target')
def scan(target): subprocess.run(['naabu', '-host', target])
@cli.command()
@click.argument('target')
def full(target): subprocess.run(['naabu', '-host', target, '-p', '-'])
if __name__ == '__main__': cli()
