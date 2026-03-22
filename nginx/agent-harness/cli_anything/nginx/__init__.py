
import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def status(): subprocess.run(['nginx', '-v'])
@cli.command()
@click.argument('config')
def test(config): subprocess.run(['nginx', '-t', '-c', config])
@cli.command()
def reload(): subprocess.run(['nginx', '-s', 'reload'])
if __name__ == '__main__': cli()
