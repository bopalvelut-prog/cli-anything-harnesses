import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('braco v39 running')
if __name__ == '__main__': cli()
