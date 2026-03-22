import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def send(): click.echo('Mailgun email sent')
@cli.command()
def logs(): click.echo('Mailgun logs')
if __name__ == '__main__': cli()
