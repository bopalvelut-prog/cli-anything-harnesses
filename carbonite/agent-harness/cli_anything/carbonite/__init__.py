import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('Carbonite status')
@cli.command()
def backup(): click.echo('Carbonite backup')
if __name__ == '__main__': cli()
