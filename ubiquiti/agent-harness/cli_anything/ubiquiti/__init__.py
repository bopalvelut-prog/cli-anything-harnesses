import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('Ubiquiti running')
@cli.command()
def devices(): click.echo('Connected devices')
if __name__ == '__main__': cli()
