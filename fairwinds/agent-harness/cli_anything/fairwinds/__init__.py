import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def insights(): click.echo('Fairwinds insights')
if __name__ == '__main__': cli()
