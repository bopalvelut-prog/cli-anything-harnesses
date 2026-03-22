import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('braco v23 running')
if __name__ == '__main__': cli()
