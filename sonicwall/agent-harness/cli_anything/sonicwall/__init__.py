import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('SonicWall running')
@cli.command()
def rules(): click.echo('Access rules')
if __name__ == '__main__': cli()
