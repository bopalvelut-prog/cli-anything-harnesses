import click
@click.group()
def cli(): pass
@cli.command()
def suggest(): click.echo('CodeWhisperer suggest')
@cli.command()
def review(): click.echo('CodeWhisperer review')
if __name__ == '__main__': cli()
