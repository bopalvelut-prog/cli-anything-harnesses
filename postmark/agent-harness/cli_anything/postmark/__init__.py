import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def send(): click.echo('Postmark email sent')
@cli.command()
def stats(): click.echo('Postmark stats')
if __name__ == '__main__': cli()
