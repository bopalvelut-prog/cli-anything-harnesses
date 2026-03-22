import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def send(): click.echo('SendGrid email sent')
@cli.command()
def list(): click.echo('SendGrid lists')
if __name__ == '__main__': cli()
