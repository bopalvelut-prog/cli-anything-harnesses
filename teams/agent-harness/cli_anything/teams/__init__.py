import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def send(): click.echo('Teams message sent')
@cli.command()
def meetings(): click.echo('Teams meetings')
if __name__ == '__main__': cli()
