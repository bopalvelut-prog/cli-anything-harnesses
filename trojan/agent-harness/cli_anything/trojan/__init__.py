import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def start(): subprocess.run(['trojan', '-c', 'config.json'])
@cli.command()
def test(): click.echo('Trojan configuration test')
if __name__ == '__main__': cli()
