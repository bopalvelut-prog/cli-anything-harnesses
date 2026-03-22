import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('Check Point running')
@cli.command()
def policy(): click.echo('Security policy')
if __name__ == '__main__': cli()
