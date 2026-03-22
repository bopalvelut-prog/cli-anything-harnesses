import click, subprocess
@click.group()
def cli(): pass
@cli.command()
@click.argument('target')
def scan(target): subprocess.run(['nikto', '-h', target])
@cli.command()
@click.argument('target')
def full(target): subprocess.run(['nikto', '-h', target, '-Tuning', 'x'])
if __name__ == '__main__': cli()
