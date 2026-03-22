import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('Cohesity status')
@cli.command()
def backup(): click.echo('Cohesity backup')
if __name__ == '__main__': cli()
