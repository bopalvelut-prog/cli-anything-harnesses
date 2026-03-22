import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('Vembu status')
@cli.command()
def backup(): click.echo('Vembu backup')
if __name__ == '__main__': cli()
