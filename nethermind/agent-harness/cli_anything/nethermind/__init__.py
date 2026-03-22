import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def start(): click.echo('Nethermind started')
if __name__ == '__main__': cli()
