import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def campaigns(): click.echo('Mailchimp campaigns')
@cli.command()
def lists(): click.echo('Mailchimp lists')
if __name__ == '__main__': cli()
