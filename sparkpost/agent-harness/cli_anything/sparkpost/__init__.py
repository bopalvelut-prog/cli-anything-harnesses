import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def send(): click.echo('SparkPost email sent')
@cli.command()
def templates(): click.echo('SparkPost templates')
if __name__ == '__main__': cli()
