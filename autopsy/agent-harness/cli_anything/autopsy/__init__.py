import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def start(): click.echo('Autopsy started')
@cli.command()
def cases(): click.echo('Autopsy cases')
if __name__ == '__main__': cli()
